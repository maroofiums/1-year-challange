from rest_framework.decorators import api_view
from rest_framework.response import Response
import pandas as pd
from .serializers import HouseInputSerializer
from .ml_model import model, label_encoders, model_columns

@api_view(['POST'])
def predict_price(request):
    serializer = HouseInputSerializer(data=request.data)
    if serializer.is_valid():
        df = pd.DataFrame([serializer.validated_data])

        for col, encoder in label_encoders.items():
            df[col] = encoder.transform(df[col])

        df = df[model_columns]

        prediction = model.predict(df)[0]

        return Response({"predicted_price": round(float(prediction), 2)})

    return Response(serializer.errors, status=400)
