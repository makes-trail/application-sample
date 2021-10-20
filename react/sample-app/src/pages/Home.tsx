import React from 'react';
import { Link } from 'react-router-dom';
import Box from '@material-ui/core/Box';
import Typography from '@material-ui/core/Typography'
import Button from '@material-ui/core/Button';
import SearchIcon from '@material-ui/icons/Search';
import LibraryBooksIcon from '@material-ui/icons/LibraryBooks';
import { createMuiTheme, ThemeProvider } from '@material-ui/core/styles';

const theme = createMuiTheme({
  typography: {
    fontFamily: [
      "游明朝体",
      "Yu Mincho",
      "YuMincho",
      "ヒラギノ明朝 Pro",
      "Hiragino Mincho Pro",
      "MS P明朝",
      "MS PMincho",
      "serif"
    ].join(",")
  }
})

const Home: React.FC = () => {
  return (
    <div>
      <ThemeProvider theme={theme}>
        <Box m={3}>
          <Typography variant="h4">MAKES TRAIL</Typography>
          <Typography variant="h5">サンプル版</Typography>
        </Box>
        <Box m={2}>
          <Button
            variant="outlined"
            size="large"
            startIcon={<SearchIcon />}
            component={Link}
            to="/search-book"
          >
            本を探す
        </Button>
        </Box>
        <Box m={2}>
          <Button
            variant="outlined"
            size="large"
            component={Link}
            startIcon={<LibraryBooksIcon />}
            to="/list-books"
          >
            図書館に入る
        </Button>
        </Box>
      </ThemeProvider>
    </div>
  )
}

export default Home;
