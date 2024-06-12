import React from "react";
import styled from '@emotion/styled'
import { Upload } from "./Upload";
import { Title2, Text, Title3 } from "@fluentui/react-components";
import { Cards } from "./Cards";
import { VerticalNav } from "./Nav";
import { SliderComponent } from "./Slider";

export const HomePage = () => {
  const [sliderValue, setSliderValue] = React.useState(0.9);

  return (
    <div className="App">
      <TopBar>
        <img src={require('../img/user.png')}  />
      </TopBar>
      <VerticalNav />
      <Blade>
          <div className="title">
            <Title2>
            Colorectal Cancer Detection
            </Title2> 
            <Text style={{marginTop: 4}}>Azure ML + TensorFlow built w/ React + Flask + Fluent2</Text>
          </div>
        <Upload />
        <div style={{height: 30}}></div>
        <Title3>Conformal Prediction</Title3>
        <SliderComponent sliderValue={sliderValue} setSliderValue={setSliderValue}/>
        <Cards threshold={sliderValue}/>
      </Blade>
    
    </div>
  );
};

const TopBar = styled.div`
  background-color: #e8f2fd;
  height: 40px;
  width: 100%;
  position: fixed;
  top: 0px;
  z-index: 100;

  img {
    height: 33px;
    top: 3px;
    right: 13px;
    position: absolute;
    border-radius: 50%;
  }
`

const Blade = styled.div`
  padding: 30px 10px 40px 0px;
  width: calc(100% - 270px);
  height: 100%;
  left: 252px;
  top: 40px;
  position: absolute;

  .title{ 
      display: block;
      margin: auto;
      width: fit-content;

      >* {
        display: block;
        text-align: center;
        margin: 10px;
      }
    }  

`