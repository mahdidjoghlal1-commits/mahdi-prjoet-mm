from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# ========================
# LOAD MODELS
# ========================
model = joblib.load("dataset/nsl_kdd_model.pkl")
scaler = joblib.load("dataset/scaler.pkl")
encoder = joblib.load("dataset/onehot_encoder.pkl")
feature_cols = joblib.load("dataset/feature_columns.pkl")

# ========================
# HOME
# ========================
@app.route('/')
def home():

    stats = {
        "baseline": 0.85,
        "attack": 0.65,
        "defense": 0.92
    }

    return render_template('index.html', stats=stats)
# ========================
# PREDICT
# ========================
@app.route('/predict', methods=['POST'])
def predict():
    try:

        # --------------------
        # NUMERICAL FEATURES
        # --------------------
        duration = float(request.form['duration'])
        src_bytes = float(request.form['src_bytes'])
        dst_bytes = float(request.form['dst_bytes'])
        count = float(request.form['count'])
        srv_count = float(request.form['srv_count'])

        X_num = np.array([[duration, src_bytes, dst_bytes, count, srv_count]])
        X_num_scaled = scaler.transform(X_num)

        # --------------------
        # CATEGORICAL FEATURES
        # --------------------
        protocol_type = request.form['protocol_type']
        service = request.form['service']
        flag = request.form['flag']

        X_cat = encoder.transform([[protocol_type, service, flag]])

        # --------------------
        # FINAL INPUT
        # --------------------
        X_final = np.hstack((X_num_scaled, X_cat))

        # FIX shape issue (very important)
        if X_final.shape[1] != model.n_features_in_:
            return render_template(
                'index.html',
                prediction_text=f"❌ Feature mismatch! Model expects {model.n_features_in_} features but got {X_final.shape[1]}"
            )

        prediction = model.predict(X_final)[0]

        result = "🚨 Attack" if prediction == 1 else "✅ Normal"

        return render_template('index.html', prediction_text=result)

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")


# ========================
# ========================
# RUN APP
# ========================
if __name__ == "__main__":
    app.run(debug=True, port=5001)
