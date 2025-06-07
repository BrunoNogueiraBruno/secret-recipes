import { Button as MUIButton, type ButtonProps } from '@mui/material';

function CustomButton(props: ButtonProps) {
  return (
    <MUIButton
      {...props}
      color="primary"
      variant={props.variant || 'contained'}
    />
  );
}

export default CustomButton;
