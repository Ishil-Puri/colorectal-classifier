import React from "react";
import styled from '@emotion/styled'
import { Upload } from "./Upload";
import { Title2, Text } from "@fluentui/react-components";
import { Cards } from "./Cards";
import { VerticalNav } from "./Nav";

export const HomePage = () => {

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
            <Text style={{marginTop: 4}}>Azure ML + TensorFlow</Text>
          </div>
        <Upload />
        <Cards />
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