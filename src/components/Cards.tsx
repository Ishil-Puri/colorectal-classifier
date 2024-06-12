import React from 'react';
import styled from '@emotion/styled';
import imagesData from '../img/test_images.json'; // Adjust the path according to your project structure

interface CardsProps {
  threshold: number;
}

interface CardProps extends React.HTMLAttributes<HTMLDivElement> {
  isAboveThreshold: boolean;
}

export const Cards: React.FC<CardsProps> = ({ threshold }) => {
  return (
    <CardContainer>
      {imagesData.map((card, index) => {
        const imagePath = require(`../img/test_images/${card.img}`);
        
        const isAboveThreshold = card.conformal_score >= threshold;

        return (
          <Card key={index} isAboveThreshold={isAboveThreshold}>
            <CardTitle>{card.title}</CardTitle>
            <img src={imagePath} alt={card.title} />
            <Score>Reliability: {card.conformal_score}</Score>
          </Card>
        );
      })}
    </CardContainer>
  );
};

const CardContainer = styled.div`
  display: flex;
  flex-wrap: wrap;
  width: 83%;
  margin: auto;
  margin-top: 30px;
`;

const Card = styled.div<CardProps>`
  width: 100px;
  height: 100px;
  padding: 20px;
  border: 5px solid ${(props) => (props.isAboveThreshold ? '#b7e4c7' : '#FBC6D1')};
  border-radius: 10px;
  margin: 10px;
  transition: transform 0.3s, box-shadow 0.3s;
  background-color: ${(props) => (props.isAboveThreshold ? '#b7e4c7' : '#FBC6D1')};

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

const Score = styled.div`
  font-size: 12px;
  text-align: center;
`;