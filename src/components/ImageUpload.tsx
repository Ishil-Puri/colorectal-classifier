import React, { useState, DragEvent } from 'react';
import styled from 'styled-components';

interface ImageUploadProps {
  onFileSelect: (file: File) => void;
}

const ImageUpload: React.FC<ImageUploadProps> = ({ onFileSelect }) => {
  const [file, setFile] = useState<File | null>(null);

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const fileList = event.target.files;
    if (fileList && fileList.length > 0) {
      const selectedFile = fileList[0];
      setFile(selectedFile);
      onFileSelect(selectedFile); // Notify the parent component
    }
  };

  const handleDragOver = (e: DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    e.stopPropagation();
  };

  const handleDrop = (e: DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    e.stopPropagation();

    const files = e.dataTransfer.files;
    if (files && files[0]) {
      const selectedFile = files[0];
      setFile(selectedFile);
      onFileSelect(selectedFile); // Notify the parent component
    }
  };

  return (
    <UploadContainer onDragOver={handleDragOver} onDrop={handleDrop}>
      {file ? (
        <ImagePreview src={URL.createObjectURL(file)} alt="Preview" />
      ) : (
        <UploadMessage>
          <div>Drag & Drop your image here</div>
          <div>or</div>
          <div>
            <label htmlFor="file-upload" style={{ cursor: 'pointer', color: '#007bff' }}>click to upload</label>
            <input id="file-upload" type="file" accept="image/*" onChange={handleFileChange} style={{ display: 'none' }} />
          </div>
        </UploadMessage>
      )}
    </UploadContainer>
  );
};

const UploadContainer = styled.div`
  border: 2px dashed #ccc;
  border-radius: 10px;
  height: 200px;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  cursor: pointer;
  margin: 20px 0;
  &:hover {
    border-color: #aaa;
  }
`;

const UploadMessage = styled.div`
  text-align: center;
  color: #aaa;
`;

const ImagePreview = styled.img`
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
  position: absolute;
`;

export default ImageUpload;