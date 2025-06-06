from flask import Flask, request, render_template
from transcript_fetcher import fetch_transcript
from analyzer import analyze_transcript
from ki_interface import run_ki_analysis
from config import USE_KI

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        link = request.form.get("ytlink")
        transcript = fetch_transcript(link)
        if transcript:
            warnings = analyze_transcript(transcript)
            result = {"warnings": warnings}
            if USE_KI:
                ki_output = run_ki_analysis(transcript)
                result["ki"] = ki_output
        else:
            result = {"error": "Kein Transkript gefunden oder ungültiger Link."}
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)