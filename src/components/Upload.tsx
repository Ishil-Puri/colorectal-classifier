import React, { useState } from "react";
import styled from '@emotion/styled'
import axios from 'axios';
import { Button } from "@fluentui/react-components";
import { useId, Label, Slider } from "@fluentui/react-components";
import type { SliderProps } from "@fluentui/react-components";

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

  //slider
  const id = useId();
  const [sliderValue, setSliderValue] = React.useState(80);
  const onSliderChange: SliderProps["onChange"] = (_, data) =>
    setSliderValue(data.value);

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const fileList = event.target.files;
    if (fileList && fileList.length > 0) {
      setFile(fileList[0]);
      setError(null); // Clear previous errors
      setPrediction(null); // Clear previous prediction
    }
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
      const response = await axios.post<PredictionResponse>('http://localhost:5001/predict', formData, {
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
        <input type="file" onChange={handleFileChange} accept="image/*" />
        <Button onClick={onSubmit} appearance="outline" disabled={!file || isLoading} title="Upload and Analyze Image">
          {isLoading ? "Analyzing..." : "Upload and Analyze"}
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
      <SliderContainer>
          <Slider value={sliderValue}
          min={0}
          max={100}
          onChange={onSliderChange}
          style={{width: 'calc(100% - 80px)'}}
          id={id}/>
        
          <Label >
            {sliderValue} 
        </Label>
      </SliderContainer>
     
    </div>
  );
}


const SliderContainer = styled.div`
  width: 490px;
  margin: auto;
  margin-top: 30px;
`
