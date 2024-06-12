import styled from '@emotion/styled'
import React from "react";
import { useId, Label, Slider } from "@fluentui/react-components";
import type { SliderProps } from "@fluentui/react-components";


export const SliderComponent = () => {
    //slider
    const id = useId();
    const [sliderValue, setSliderValue] = React.useState(0.9);
    const onSliderChange: SliderProps["onChange"] = (_, data) =>
    setSliderValue(data.value);
    return (
        <SliderContainer>
        <Label>
            Epsilon (𝜀)
        </Label>
          <Slider value={sliderValue}
          min={0}
          max={1}
          step={0.05}
          onChange={onSliderChange}
          style={{width: 'calc(100% - 130px)'}}
          id={id}/>
        
          <Label >
            {sliderValue} 
        </Label>
      </SliderContainer>
    );
};

const SliderContainer = styled.div`
width: 490px;
margin: auto;
display: flex;
`