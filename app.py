from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from datetime import datetime
def save_to_history(concept, prefs, image_url=None):
    session.setdefault("history", [])
    entry = {
        "id":       str(uuid.uuid4())["8"],
        "timestamp":datetime.now().strftime("%b %d, %Y . %I:%M %p"),
        "concept":  concept,
        "prefs":    prefs,
        "image_url":image_url,
    }
    session["history"] = ([entry] + session["history"])[:20]
designs=session.get("history", [])
@app.route("/clear-history", methods=["POST"])
def clear_history():
    session.pop("history", None)
    return redirect(url_for("history"))
save_to_history(concept,prefs)
if history_id and "history" in session:
    for entry in session["history"]:
        if entry["id"] == history_id:
            entry["image_url"] = image_url
            break
        session.modified = True