import Box from '@material-ui/core/Box';
import Button from '@material-ui/core/Button';
import ButtonGroup from '@material-ui/core/ButtonGroup';
import { createMuiTheme, ThemeProvider } from '@material-ui/core/styles';
import LibraryBooksIcon from '@material-ui/icons/LibraryBooks';
import SearchIcon from '@material-ui/icons/Search';
import React from 'react';
import { Link } from 'react-router-dom';

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
          <h1 className="font-yumin">MAKES TRAIL</h1>
          <h2 className="font-yumin">サンプル版</h2>
        </Box>
        <Box m={2}>
          <ButtonGroup
            orientation="vertical"
            aria-label="vertical outlined button group"
          >
            <Button
              size="large"
              startIcon={<SearchIcon />}
              component={Link}
              to="/search-book"
            >
              本を探す
            </Button>
            <Button
              size="large"
              component={Link}
              startIcon={<LibraryBooksIcon />}
              to="/list-books"
            >
              図書館に入る
            </Button>
          </ButtonGroup>
        </Box>
      </ThemeProvider>
    </div>
  )
}

export default Home;
