from flask import Flask, send_file, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client["truck_inspections"]
images_collection = db["images"]

@app.route('/image/<filename>')
def get_image(filename):
    image_data = images_collection.find_one({"filename": filename})
    if image_data:
        return send_file(image_data["image_path"], mimetype='image/png')
    else:
        return jsonify({"error": "Image not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
