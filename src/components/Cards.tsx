import React from 'react';
import styled from '@emotion/styled'

export const Cards = () => {
    const cards = [
        { title: 'Card Title',  img: 'test-img.png' },
        { title: 'Card Title',  img: 'test-img.png' },
        { title: 'Card Title',  img: 'test-img.png' },
        { title: 'Card Title',  img: 'test-img.png' },
        { title: 'Card Title',  img: 'test-img.png' },
        { title: 'Card Title',  img: 'test-img.png' },
        { title: 'Card Title',  img: 'test-img.png' },
        { title: 'Card Title',  img: 'test-img.png' },
        { title: 'Card Title',  img: 'test-img.png' },
        { title: 'Card Title',  img: 'test-img.png' },
        { title: 'Card Title',  img: 'test-img.png' },
        { title: 'Card Title',  img: 'test-img.png' },
        { title: 'Card Title',  img: 'test-img.png' },
        { title: 'Card Title',  img: 'test-img.png' },
        { title: 'Card Title',  img: 'test-img.png' },
        { title: 'Card Title',  img: 'test-img.png' },
        { title: 'Card Title',  img: 'test-img.png' },
        { title: 'Card Title',  img: 'test-img.png' },
        { title: 'Card Title',  img: 'test-img.png' },
        { title: 'Card Title',  img: 'test-img.png' },
        { title: 'Card Title',  img: 'test-img.png' },
        { title: 'Card Title',  img: 'test-img.png' },
        { title: 'Card Title',  img: 'test-img.png' },
        { title: 'Card Title',  img: 'test-img.png' },
        { title: 'Card Title',  img: 'test-img.png' },
        { title: 'Card Title',  img: 'test-img.png' },
        { title: 'Card Title',  img: 'test-img.png' },
        { title: 'Card Title',  img: 'test-img.png' },
        { title: 'Card Title',  img: 'test-img.png' },
        { title: 'Card Title',  img: 'test-img.png' },
        { title: 'Card Title',  img: 'test-img.png' },
        { title: 'Card Title',  img: 'test-img.png' },
        { title: 'Card Title',  img: 'test-img.png' },
        { title: 'Card Title',  img: 'test-img.png' },
        { title: 'Card Title',  img: 'test-img.png' },
        { title: 'Card Title',  img: 'test-img.png' },
      ];
  return (
    <CardContainer>
    {cards.map((card, index) => (
        <Card key={index}>
          <CardTitle>{card.title}</CardTitle>
          <img src={require(`../img/${card.img}`)} /> 
        </Card>
      ))}
    </CardContainer>
  );
};

const CardContainer = styled.div`
    display:flex;
    flex-flow: wrap;
    width: 83%;
    margin: auto;
    margin-top:30px;
`
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

    :hover{
        cursor: pointer;
        box-shadow: 8px 7px 7px -5px rgba(0,0,0,0.36);
        transform: scale(1.1) translate(0%, 0%);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    }
`

const CardTitle = styled.div`

`