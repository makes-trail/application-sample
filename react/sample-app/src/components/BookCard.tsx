import { useState } from 'react';
import { Book } from '../types/Book';
import Typography from '@material-ui/core/Typography';
import Card from '@material-ui/core/Card';
import CardHeader from '@material-ui/core/CardHeader';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import IconButton from '@material-ui/core/IconButton';
import FavoriteIcon from '@material-ui/icons/Favorite';
import { makeStyles } from '@material-ui/core';

const useStyles = makeStyles({
  root: {
    margin: 'auto',
    maxWidth: 300
  },
  cover: {
    height: 180,
  }
});

const BookCard: React.FC<{ book: Book }> = ({ book }) => {
  const classes = useStyles();
  const [isFavorite, setIsFavorite] = useState<boolean>(false);

  return (
    <div>
      <Card className={classes.root} elevation={2}>
        <CardHeader
          title={
            <Typography variant="h6" component="p">
              {book.title}
            </Typography>
          }
          subheader={book.author}
          action={
            <IconButton onClick={() => setIsFavorite(!isFavorite)}>
              <FavoriteIcon color={isFavorite ? "secondary" : "inherit"} />
            </IconButton>
          }
        />
        <CardMedia
          className={classes.cover}
          image={book.cover ? book.cover : '/assets/image/book_icon_300x300.png'}
        />
        <CardContent>
          <Typography>
            {book.publisher}
          </Typography>
          <Typography variant="body2" color="textSecondary">
            ISBN {book.isbn}
          </Typography>
        </CardContent>
      </Card>
    </div>
  );
}

export default BookCard;
