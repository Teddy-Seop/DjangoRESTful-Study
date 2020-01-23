import React from 'react';
import { Link } from 'react-router-dom';

class Home extends React.Component {
    state = {
        posts: []
    };

    async componentDidMount() {
        try {
            const res = await fetch('http://127.0.0.1:8000/posts');
            const posts = await res.json();
            this.setState({
                posts
            });
        } catch (e) {
            console.log(e);
        }
    }

    post = event => {
        fetch('http://127.0.0.1:8000/posts/create', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(this.state.posts)
      });
    }

    render() {
        return (
            <div>
              {this.state.posts.map(item => (
                <div key={item.id}>
                  <h1><Link to={"/Detail/" + item.id}>{item.title}</Link></h1>
                  <span>{item.content}</span>
                </div>
              ))}
              <button><Link to="/Write">WRITE</Link></button>
            </div>
        );
    }
}

export default Home;
