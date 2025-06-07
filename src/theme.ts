import { createTheme } from '@mui/material/styles';

const theme = createTheme({
  palette: {
    primary: {
      main: '#8BC34A',      // Verde fresco (alface, ervas)
      light: '#C5E1A5',
      dark: '#689F38',
      contrastText: '#ffffff',
    },
    secondary: {
      main: '#FF7043',      // Laranja queimado (cenoura assada, temperos)
      light: '#FFA270',
      dark: '#C63F17',
      contrastText: '#ffffff',
    },
    background: {
      default: '#FFF8F0',   // Fundo creme claro (papel de receita)
      paper: '#FFFFFF',
    },
    error: {
      main: '#D32F2F',      // Erros/sinais de atenção
    },
    warning: {
      main: '#FBC02D',
    },
    info: {
      main: '#0288D1',
    },
    success: {
      main: '#388E3C',
    },
    text: {
      primary: '#3E3E3E',
      secondary: '#7B7B7B',
    },
  },
});

export default theme