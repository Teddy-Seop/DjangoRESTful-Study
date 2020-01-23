import React from 'react';

class Detail extends React.Component {
    state = {
        posts: []
    };
    async componentWillMount(props) {
        try {
          var url = 'http://127.0.0.1:8000/posts/' + this.props.match.params.id;
          const res = await fetch(url)
          // .then(response => response.json())
          // .then(json => console.log(json))
          // .catch(err => console.log(err));
          console.log(res)
          const posts = await res.json();
          console.log(posts)
          this.setState({
              posts
          });
        } catch (e) {
            console.log(e);
        }
    }
    render(){
        return (
          <div>
            <div>
              <div key={0}>
                <h1>{this.state.posts.title}</h1>
                <span>{this.state.posts.content}</span>
              </div>
            </div>
          </div>
        );
    }
}

export default Detail;
