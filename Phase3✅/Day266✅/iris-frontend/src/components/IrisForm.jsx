import { useState } from "react";
import axios from "axios";

const API_URL = "http://127.0.0.1:8000/predict";

function IrisForm() {
  const [formData, setFormData] = useState({
    sepal_length: "",
    sepal_width: "",
    petal_length: "",
    petal_width: "",
  });
  const [result, setResult] = useState("");

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post(API_URL, {
        sepal_length: parseFloat(formData.sepal_length),
        sepal_width: parseFloat(formData.sepal_width),
        petal_length: parseFloat(formData.petal_length),
        petal_width: parseFloat(formData.petal_width),
      });
      setResult(res.data.prediction);
    } catch (error) {
      console.error(error);
      setResult("❌ Error while predicting");
    }
  };

  return (
    <form onSubmit={handleSubmit} className="flex flex-col gap-3">
      {["sepal_length", "sepal_width", "petal_length", "petal_width"].map(
        (field) => (
          <input
            key={field}
            type="number"
            step="any"
            name={field}
            placeholder={field.replace("_", " ")}
            value={formData[field]}
            onChange={handleChange}
            required
            className="p-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500"
          />
        )
      )}

      <button
        type="submit"
        className="mt-3 bg-green-600 text-white py-2 rounded-lg hover:bg-green-700 transition"
      >
        Predict
      </button>

      {result && (
        <p className="mt-4 text-center text-lg font-semibold text-blue-700">
          Result: {result}
        </p>
      )}
    </form>
  );
}

export default IrisForm;
