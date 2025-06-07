import { TextField, type TextFieldProps } from '@mui/material';

function Input(props: TextFieldProps) {
  return (
    <TextField
      {...props}
      color="primary"
      className={`${props.className} `}
      size='small'
    />
  );
}

export default Input;
