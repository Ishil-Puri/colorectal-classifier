import React from "react";
import styled from '@emotion/styled'
import { Upload } from "./Upload";
import { Title2, Text } from "@fluentui/react-components";
import { Cards } from "./Cards";

export const HomePage = () => {


  return (
    <div className="App">
      <TopBar>
      </TopBar>
      <Blade>
          <Title2>
            Colorectal Cancer Detection
          </Title2> 
          <Text style={{marginTop: 4}}>Azure ML + TensorFlow</Text>
      </Blade>
      <Upload />
      <Cards />
    </div>
  );
};

const TopBar = styled.div`
  background-color: #e8f2fd;
  height: 40px;
  width: 100%;
  position: absolute;
  top: 0px;
`

const Blade = styled.div`
padding: 80px 10px 40px 10px;
width: 100%;
height: 100%;

  > *
    {
      display: block;
      margin: auto;
      width: fit-content;
    }  

`