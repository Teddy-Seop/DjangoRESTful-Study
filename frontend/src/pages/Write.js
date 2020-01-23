import React from 'react';

class Write extends React.Component {
  state = {
    title: 'a',
    content: 'b',
    writer:'c'
  };

  handleSubmit = (event) => {
        alert('submit');
        fetch('http://127.0.0.1:8000/posts/create', {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify(this.state)
        })
        .then(res => res.json())
        // .then(note => {
        //   return dispatch({
        //     type: 'ADD_NOTE',
        //     note
        //   })
        // })
        // axios.post(url, body, headers)
        // .then((response) => {
        //     if (response.data.email_confirmed) this.setState({emailConfirmed: true});
        // }).catch(error => {
        //     console.log("ERROR", error)
        // });
    };

  render() {
    return(
      <div>
        <form onSubmit={this.handleSubmit}>
          <div>
            <input type="text"/>
            <textarea placeholder="Write down your memo"></textarea>
          </div>
          <div>
            <button type="submit">WRITE</button>
          </div>
        </form>
      </div>
    );
  }
}

export default Write;
