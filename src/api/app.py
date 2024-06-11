from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
import numpy as np

app = Flask(__name__)
CORS(app)  # Handle CORS if accessing from different origins
print("tf_version: " + tf.__version__)
model = tf.keras.models.load_model('./colo_model2.h5')


@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    if not allowed_file(file.filename):
        return jsonify({"error": "File type not allowed"}), 400
    
    try:
        image = tf.io.decode_image(file.read(), channels=3)
        image = tf.image.resize(image, [224, 224])
        image = image / 255.0  # Normalize image
        image = tf.expand_dims(image, axis=0)  # Add batch dimension

        predictions = model.predict(image)
        predicted_class = np.argmax(predictions, axis=1)[0]
        confidence = predictions[0][predicted_class]

        reliability = get_conformal_prediction(predictions[0])

        response = {
            'predicted_class': int(predicted_class),
            'predicted_class_name': class_names[predicted_class],
            'confidence': float(confidence),
            'reliability': str(f"{reliability[0]}, {reliability[1]}")
        }

        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg'}


calibration_nonconformity_scores = np.loadtxt('calibration_non_conformity_scores.txt')
confidence_level = 0.4
threshold = np.quantile(calibration_nonconformity_scores, 1 - confidence_level)
print(f"Threshold for {confidence_level*100}% confidence level: {threshold}")

def get_conformal_prediction(predictions) -> list:
    max_p = np.max(predictions)
    nonconformity_score = 1 - max_p
    print(f"Nonconformity score: {nonconformity_score}")
    reliability_percentile = 1 - np.searchsorted(np.sort(calibration_nonconformity_scores), nonconformity_score) / len(calibration_nonconformity_scores)

    isReliable = nonconformity_score <= threshold
    return [isReliable, np.round(reliability_percentile, 2)]
    


class_names = {0: 'tumour epithelium', 1: 'simple stroma',
               2: 'complex stroma', 3: 'immune cell conglomerates',
               4: 'debris and mucus', 5: 'mucosal glands',
               6: 'adipose tissue', 7: 'background'}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
