import React, { useState } from "react";
import axios from 'axios';
import { Button } from "@fluentui/react-components";
import ImageUpload from './ImageUpload';

interface PredictionResponse {
  predicted_class: number;
  predicted_class_name: string;
  confidence: number;
  reliability: number;
}

export const Upload = () => {
  const [file, setFile] = useState<File | null>(null);
  const [lastProcessedFile, setLastProcessedFile] = useState<File | null>(null);
  const [prediction, setPrediction] = useState<PredictionResponse | null>(null);
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  
  const handleFileSelect = (selectedFile: File) => {
    setFile(selectedFile);
    setError(null); // Clear previous errors
    setPrediction(null); // Clear previous prediction
  };

  const onSubmit = async () => {
    if (!file) {
      setError("Please upload an image file.");
      return;
    }
    if (file === lastProcessedFile) {
      setError("Please choose a new file to analyze.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    setIsLoading(true);
    setError(null);

    try {
      const response = await axios.post<PredictionResponse>('http://localhost:5001/scoring', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
      setPrediction(response.data);
      setLastProcessedFile(file); // Update the last processed file
    } catch (error: any) {
      setError(error.response?.data || "An unexpected error occurred.");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div>
      <div className="block upload">
        <ImageUpload onFileSelect={handleFileSelect} />
        <Button onClick={onSubmit} appearance="outline" disabled={!file || isLoading} title="Upload and Analyze Image">
          {isLoading ? "Analyzing..." : "Analyze"}
        </Button>
      </div>
      
      {error && <p>Error: {error}</p>}
      {prediction && (
        <div>
          <p>Predicted Class: {prediction.predicted_class} — {prediction.predicted_class_name}</p>
          <p>Confidence: {prediction.confidence.toFixed(2)}</p>
          <p>Conformal Reliability: {prediction.reliability}</p>
        </div>
      )}
      
     
    </div>
  );
};
