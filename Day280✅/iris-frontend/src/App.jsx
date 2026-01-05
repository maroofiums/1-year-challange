import IrisForm from "./components/IrisForm";

function App() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-r from-green-200 to-blue-200">
      <div className="bg-white p-8 rounded-2xl shadow-lg w-[400px]">
        <h1 className="text-2xl font-bold text-center mb-6 text-green-700">
          🌸 Iris Flower Predictor
        </h1>
        <IrisForm />
      </div>
    </div>
  );
}

export default App;
