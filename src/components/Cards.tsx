import React from 'react';
import styled from '@emotion/styled';
import imagesData from '../img/test_images.json'; // Adjust the path according to your project structure

export const Cards = () => {
  return (
    <CardContainer>
      {imagesData.map((card, index) => {
        const imagePath = require(`../img/test_images/${card.img}`);
        console.log('Image Path:', imagePath); // Debugging: Check the image paths
        return (
          <Card key={index}>
            <CardTitle>{card.title}</CardTitle>
            <img src={imagePath} alt={card.title} />
          </Card>
        );
      })}
    </CardContainer>
  );
};

const CardContainer = styled.div`
  display: flex;
  flex-flow: wrap;
  width: 83%;
  margin: auto;
  margin-top: 30px;
`;

const Card = styled.div`
  width: 100px;
  height: 100px;
  padding: 10px;
  border: 3px solid #eeeeee;
  border-radius: 10px;
  margin: 10px;
  transition: transform 0.3s, box-shadow 0.3s;

  img {
    width: 70px;
    height: 70px;
    margin-top: 5px;
  }

  &:hover {
    cursor: pointer;
    box-shadow: 8px 7px 7px -5px rgba(0, 0, 0, 0.36);
    transform: scale(1.1) translate(0%, 0%);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
  }
`;

const CardTitle = styled.div`
  font-size: 14px;
  text-align: center;
`;