import React, { Component} from 'react';

class Test extends Component {
    state = {
        posts: {title: '', content: ''}
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


              <input type="text" name="title"
              value={this.state.posts.title}/>

              <input type="text" name="content"
              value={this.state.posts.content}/>

              <br/>
              <button onClick={this.post}>POST</button>
            </div>
        );
    }
}

export default Test;

