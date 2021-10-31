import { User } from '../types/User';
import Card from '@material-ui/core/Card';
import CardHeader from '@material-ui/core/CardHeader';
import CardMedia from '@material-ui/core/CardMedia';
import { makeStyles } from '@material-ui/core';

const useStyles = makeStyles({
  root: {
    margin: '50px auto',
    maxWidth: 400,
    boxShadow: '5px 5px 5px rgba(0,0,0,0.3)'
  },
  header: {
    backgroundColor: '#dddddd',
  },
  cover: {
    height: 300,
  }
});

const UserCard: React.FC<{ user: User }> = ({ user }) => {
  const classes = useStyles();

  return (
    <div>
      <Card className={classes.root} elevation={2}>
        <CardHeader
          className={classes.header}
          title={user.name}
          subheader={user.userId}
        />
        <CardMedia
          className={classes.cover}
          image={user.iconUrl}
        />
      </Card>
    </div>
  );
}

export default UserCard;
