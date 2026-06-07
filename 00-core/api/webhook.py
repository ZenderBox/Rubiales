"""Webhook receptor de updates desde tareas.html + módulo Documentos (Miramar)."""
import os
import uuid
from datetime import datetime
from pathlib import Path

from flask import Flask, request, jsonify, send_from_directory, abort
import psycopg2
import psycopg2.extras


app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 50 * 1024 * 1024  # 50 MB

DB_CONFIG = {
    "host": "localhost",
    "dbname": "miramar",
    "user": "miramar_admin",
    "password": "MiramarAdmin2026!",
}

PHOTOS_DIR = Path("/opt/miramar/photos")
PHOTOS_DIR.mkdir(parents=True, exist_ok=True)

DOCUMENTS_DIR = Path("/opt/miramar/documents")
DOCUMENTS_DIR.mkdir(parents=True, exist_ok=True)

ALLOWED_UPDATE_TYPES = {"done", "note", "photo"}
ALLOWED_PHOTO_EXT = {".jpg", ".jpeg", ".png", ".heic", ".webp"}
ALLOWED_DOC_EXT = {
    ".pdf", ".jpg", ".jpeg", ".png", ".heic", ".webp",
    ".xls", ".xlsx", ".csv",
    ".doc", ".docx",
    ".txt", ".rtf",
    ".zip",
}
ALLOWED_CATEGORIES = {
    "regulatorio", "finanzas", "predio",
    "comercial", "operacion", "sin-clasificar"
}


def db():
    return psycopg2.connect(**DB_CONFIG)


# ============================================================
# Health
# ============================================================
@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "time": datetime.utcnow().isoformat()})


# ============================================================
# Tareas · updates de papá
# ============================================================
@app.route("/api/update", methods=["POST"])
def update():
    task_id = (request.form.get("task_id") or "").strip()
    update_type = (request.form.get("update_type") or "").strip()
    note = (request.form.get("note") or "").strip()
    submitter = (request.form.get("submitter") or "papa").strip()[:50]

    if not task_id or update_type not in ALLOWED_UPDATE_TYPES:
        return jsonify({"error": "invalid_payload"}), 400

    photo_path = None
    photo = request.files.get("photo")
    if photo and photo.filename:
        ext = Path(photo.filename).suffix.lower()
        if ext not in ALLOWED_PHOTO_EXT:
            return jsonify({"error": "invalid_photo_type"}), 400
        ts = datetime.utcnow().strftime("%Y%m%d-%H%M%S")
        fname = f"{ts}-{uuid.uuid4().hex[:8]}{ext}"
        full = PHOTOS_DIR / fname
        photo.save(str(full))
        os.chmod(str(full), 0o644)
        photo_path = f"/photos/{fname}"

    try:
        conn = db()
        with conn, conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO pending_updates
                    (task_id, update_type, note, photo_path, submitter)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING id
                """,
                (task_id, update_type, note or None, photo_path, submitter),
            )
            new_id = cur.fetchone()[0]
        conn.close()
        return jsonify({"ok": True, "id": new_id, "photo_path": photo_path})
    except Exception as exc:
        return jsonify({"error": "db_error", "detail": str(exc)}), 500


@app.route("/api/pending", methods=["GET"])
def pending():
    try:
        conn = db()
        with conn, conn.cursor() as cur:
            cur.execute(
                """
                SELECT id, task_id, update_type, note, photo_path, submitter, submitted_at
                FROM pending_updates
                WHERE status = 'pending'
                ORDER BY submitted_at DESC
                """
            )
            rows = [
                {
                    "id": r[0], "task_id": r[1], "update_type": r[2],
                    "note": r[3], "photo_path": r[4], "submitter": r[5],
                    "submitted_at": r[6].isoformat() if r[6] else None,
                }
                for r in cur.fetchall()
            ]
        conn.close()
        return jsonify({"updates": rows})
    except Exception as exc:
        return jsonify({"error": "db_error", "detail": str(exc)}), 500


# ============================================================
# Documentos
# ============================================================
@app.route("/api/documents", methods=["GET"])
def list_documents():
    """Lista los documentos activos · filtros opcionales."""
    category = request.args.get("category")
    task_id = request.args.get("task_id")
    q = request.args.get("q", "").strip()

    sql = """
        SELECT id, filename, original_name, mime_type, size_bytes,
               category, related_task_id, related_module,
               uploaded_by, uploaded_at, note
        FROM documents
        WHERE deleted_at IS NULL
    """
    params = []
    if category:
        sql += " AND category = %s"
        params.append(category)
    if task_id:
        sql += " AND related_task_id = %s"
        params.append(task_id)
    if q:
        sql += " AND (original_name ILIKE %s OR note ILIKE %s)"
        like = f"%{q}%"
        params.extend([like, like])
    sql += " ORDER BY uploaded_at DESC"

    try:
        conn = db()
        with conn, conn.cursor() as cur:
            cur.execute(sql, params)
            rows = []
            for r in cur.fetchall():
                rows.append({
                    "id": r[0],
                    "filename": r[1],
                    "original_name": r[2],
                    "mime_type": r[3],
                    "size_bytes": r[4],
                    "category": r[5],
                    "related_task_id": r[6],
                    "related_module": r[7],
                    "uploaded_by": r[8],
                    "uploaded_at": r[9].isoformat() if r[9] else None,
                    "note": r[10],
                })
        conn.close()
        return jsonify({"documents": rows})
    except Exception as exc:
        return jsonify({"error": "db_error", "detail": str(exc)}), 500


@app.route("/api/documents/upload", methods=["POST"])
def upload_document():
    """Subir un nuevo documento."""
    f = request.files.get("file")
    if not f or not f.filename:
        return jsonify({"error": "no_file"}), 400

    ext = Path(f.filename).suffix.lower()
    if ext not in ALLOWED_DOC_EXT:
        return jsonify({"error": "invalid_file_type", "allowed": sorted(ALLOWED_DOC_EXT)}), 400

    category = (request.form.get("category") or "sin-clasificar").strip().lower()
    if category not in ALLOWED_CATEGORIES:
        category = "sin-clasificar"
    related_task = (request.form.get("related_task_id") or "").strip() or None
    related_module = (request.form.get("related_module") or "").strip() or None
    uploaded_by = (request.form.get("uploaded_by") or "papa").strip()[:50]
    note = (request.form.get("note") or "").strip() or None

    ts = datetime.utcnow().strftime("%Y%m%d-%H%M%S")
    stored_name = f"{ts}-{uuid.uuid4().hex[:8]}{ext}"
    full = DOCUMENTS_DIR / stored_name
    f.save(str(full))
    os.chmod(str(full), 0o644)
    size_bytes = full.stat().st_size

    try:
        conn = db()
        with conn, conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO documents
                    (filename, original_name, mime_type, size_bytes,
                     category, related_task_id, related_module,
                     uploaded_by, note)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING id
                """,
                (stored_name, f.filename, f.mimetype, size_bytes,
                 category, related_task, related_module,
                 uploaded_by, note),
            )
            new_id = cur.fetchone()[0]
        conn.close()
        return jsonify({"ok": True, "id": new_id, "filename": stored_name})
    except Exception as exc:
        # Si la DB falla, borramos el archivo subido
        try:
            full.unlink()
        except Exception:
            pass
        return jsonify({"error": "db_error", "detail": str(exc)}), 500


@app.route("/api/documents/<int:doc_id>/file", methods=["GET"])
def get_document_file(doc_id):
    """Descargar / mostrar el archivo de un documento."""
    try:
        conn = db()
        with conn, conn.cursor() as cur:
            cur.execute(
                """
                SELECT filename, original_name, mime_type
                FROM documents
                WHERE id = %s AND deleted_at IS NULL
                """,
                (doc_id,),
            )
            row = cur.fetchone()
        conn.close()
        if not row:
            return jsonify({"error": "not_found"}), 404
        filename, original_name, mime_type = row
        return send_from_directory(
            str(DOCUMENTS_DIR),
            filename,
            mimetype=mime_type,
            as_attachment=False,
            download_name=original_name,
        )
    except Exception as exc:
        return jsonify({"error": "server_error", "detail": str(exc)}), 500


@app.route("/api/documents/<int:doc_id>", methods=["PATCH"])
def update_document(doc_id):
    """Actualizar metadata del documento (categoría, tarea relacionada, nota)."""
    data = request.get_json(silent=True) or {}
    allowed = {"category", "related_task_id", "related_module", "note"}
    sets = []
    params = []
    for k in allowed:
        if k in data:
            if k == "category":
                v = (data[k] or "sin-clasificar").strip().lower()
                if v not in ALLOWED_CATEGORIES:
                    v = "sin-clasificar"
                sets.append("category = %s")
                params.append(v)
            else:
                sets.append(f"{k} = %s")
                params.append(data[k])
    if not sets:
        return jsonify({"error": "nothing_to_update"}), 400
    params.append(doc_id)
    sql = f"UPDATE documents SET {', '.join(sets)} WHERE id = %s AND deleted_at IS NULL"
    try:
        conn = db()
        with conn, conn.cursor() as cur:
            cur.execute(sql, params)
            updated = cur.rowcount
        conn.close()
        if updated == 0:
            return jsonify({"error": "not_found"}), 404
        return jsonify({"ok": True, "updated": updated})
    except Exception as exc:
        return jsonify({"error": "db_error", "detail": str(exc)}), 500


@app.route("/api/documents/<int:doc_id>", methods=["DELETE"])
def delete_document(doc_id):
    """Soft-delete · marca deleted_at."""
    try:
        conn = db()
        with conn, conn.cursor() as cur:
            cur.execute(
                "UPDATE documents SET deleted_at = NOW() WHERE id = %s AND deleted_at IS NULL",
                (doc_id,),
            )
            updated = cur.rowcount
        conn.close()
        if updated == 0:
            return jsonify({"error": "not_found"}), 404
        return jsonify({"ok": True})
    except Exception as exc:
        return jsonify({"error": "db_error", "detail": str(exc)}), 500


# ============================================================
# Ideas · papá apunta cosas sueltas (viajes, ideas, recordatorios)
# ============================================================
@app.route("/api/ideas", methods=["GET"])
def list_ideas():
    status = request.args.get("status", "open")
    try:
        conn = db()
        with conn, conn.cursor() as cur:
            if status == "all":
                cur.execute(
                    "SELECT id, title, body, category, submitter, status, photo_path, created_at "
                    "FROM ideas ORDER BY created_at DESC"
                )
            else:
                cur.execute(
                    "SELECT id, title, body, category, submitter, status, photo_path, created_at "
                    "FROM ideas WHERE status = %s ORDER BY created_at DESC",
                    (status,),
                )
            rows = [
                {
                    "id": r[0], "title": r[1], "body": r[2], "category": r[3],
                    "submitter": r[4], "status": r[5], "photo_path": r[6],
                    "created_at": r[7].isoformat() if r[7] else None,
                }
                for r in cur.fetchall()
            ]
        conn.close()
        return jsonify({"ideas": rows})
    except Exception as exc:
        return jsonify({"error": "db_error", "detail": str(exc)}), 500


@app.route("/api/ideas", methods=["POST"])
def create_idea():
    title = (request.form.get("title") or "").strip()
    body = (request.form.get("body") or "").strip()
    category = (request.form.get("category") or "general").strip().lower()
    submitter = (request.form.get("submitter") or "papa").strip()[:50]
    if not title:
        return jsonify({"error": "title_required"}), 400

    photo_path = None
    photo = request.files.get("photo")
    if photo and photo.filename:
        ext = Path(photo.filename).suffix.lower()
        if ext in ALLOWED_PHOTO_EXT:
            ts = datetime.utcnow().strftime("%Y%m%d-%H%M%S")
            fname = f"idea-{ts}-{uuid.uuid4().hex[:8]}{ext}"
            full = PHOTOS_DIR / fname
            photo.save(str(full))
            os.chmod(str(full), 0o644)
            photo_path = f"/photos/{fname}"

    try:
        conn = db()
        with conn, conn.cursor() as cur:
            cur.execute(
                "INSERT INTO ideas (title, body, category, submitter, photo_path) "
                "VALUES (%s, %s, %s, %s, %s) RETURNING id",
                (title, body or None, category, submitter, photo_path),
            )
            new_id = cur.fetchone()[0]
        conn.close()
        return jsonify({"ok": True, "id": new_id, "photo_path": photo_path})
    except Exception as exc:
        return jsonify({"error": "db_error", "detail": str(exc)}), 500


@app.route("/api/ideas/<int:idea_id>", methods=["PATCH"])
def update_idea(idea_id):
    new_status = (request.form.get("status") or request.json.get("status") if request.is_json else request.form.get("status") or "").strip()
    if new_status not in {"open", "done", "archived"}:
        return jsonify({"error": "invalid_status"}), 400
    try:
        conn = db()
        with conn, conn.cursor() as cur:
            cur.execute(
                "UPDATE ideas SET status = %s, updated_at = NOW() WHERE id = %s",
                (new_status, idea_id),
            )
            updated = cur.rowcount
        conn.close()
        if updated == 0:
            return jsonify({"error": "not_found"}), 404
        return jsonify({"ok": True})
    except Exception as exc:
        return jsonify({"error": "db_error", "detail": str(exc)}), 500


# ============================================================
# Ideas · Comentarios y edición
# ============================================================
@app.route("/api/ideas/<int:idea_id>/comments", methods=["GET"])
def list_idea_comments(idea_id):
    try:
        conn = db()
        with conn, conn.cursor() as cur:
            cur.execute(
                "SELECT id, body, submitter, photo_path, created_at "
                "FROM idea_comments WHERE idea_id = %s ORDER BY created_at ASC",
                (idea_id,),
            )
            rows = [
                {
                    "id": r[0], "body": r[1], "submitter": r[2],
                    "photo_path": r[3],
                    "created_at": r[4].isoformat() if r[4] else None,
                }
                for r in cur.fetchall()
            ]
        conn.close()
        return jsonify({"comments": rows})
    except Exception as exc:
        return jsonify({"error": "db_error", "detail": str(exc)}), 500


@app.route("/api/ideas/<int:idea_id>/comments", methods=["POST"])
def add_idea_comment(idea_id):
    body = (request.form.get("body") or "").strip()
    submitter = (request.form.get("submitter") or "papa").strip()[:50]
    if not body and not request.files.get("photo"):
        return jsonify({"error": "body_or_photo_required"}), 400

    photo_path = None
    photo = request.files.get("photo")
    if photo and photo.filename:
        ext = Path(photo.filename).suffix.lower()
        if ext in ALLOWED_PHOTO_EXT:
            ts = datetime.utcnow().strftime("%Y%m%d-%H%M%S")
            fname = f"idea-cmt-{ts}-{uuid.uuid4().hex[:8]}{ext}"
            full = PHOTOS_DIR / fname
            photo.save(str(full))
            os.chmod(str(full), 0o644)
            photo_path = f"/photos/{fname}"

    try:
        conn = db()
        with conn, conn.cursor() as cur:
            # Verificar que existe la idea
            cur.execute("SELECT 1 FROM ideas WHERE id = %s", (idea_id,))
            if not cur.fetchone():
                conn.close()
                return jsonify({"error": "idea_not_found"}), 404
            cur.execute(
                "INSERT INTO idea_comments (idea_id, body, submitter, photo_path) "
                "VALUES (%s, %s, %s, %s) RETURNING id",
                (idea_id, body or "", submitter, photo_path),
            )
            new_id = cur.fetchone()[0]
            # Touch updated_at de la idea
            cur.execute("UPDATE ideas SET updated_at = NOW() WHERE id = %s", (idea_id,))
        conn.close()
        return jsonify({"ok": True, "id": new_id, "photo_path": photo_path})
    except Exception as exc:
        return jsonify({"error": "db_error", "detail": str(exc)}), 500


@app.route("/api/ideas/<int:idea_id>/edit", methods=["POST"])
def edit_idea(idea_id):
    """Editar título / body / categoría de una idea."""
    title = (request.form.get("title") or "").strip()
    body = (request.form.get("body") or "").strip()
    category = (request.form.get("category") or "").strip().lower()
    if not title:
        return jsonify({"error": "title_required"}), 400
    try:
        conn = db()
        with conn, conn.cursor() as cur:
            cur.execute(
                "UPDATE ideas SET title = %s, body = %s, category = COALESCE(NULLIF(%s, ''), category), updated_at = NOW() "
                "WHERE id = %s",
                (title, body or None, category, idea_id),
            )
            updated = cur.rowcount
        conn.close()
        if updated == 0:
            return jsonify({"error": "not_found"}), 404
        return jsonify({"ok": True})
    except Exception as exc:
        return jsonify({"error": "db_error", "detail": str(exc)}), 500


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5050, debug=False)
