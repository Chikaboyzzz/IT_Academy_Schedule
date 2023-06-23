import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.min.js';

import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Schedule() {
  const [myData, setMyData] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/lesson/')
      .then(response => {
        setMyData(response.data);
      })
      .catch(error => {
        console.error('Error fetching lesson:', error);
      });
  }, []);

  return (
    <div>
      <h1>Lesson</h1>
      {myData.map((lesson) => {
      const {id,date,group,mentor,viewer} = lesson;
        return (
        <div key={id}>
          <p>Date: {date}</p>
          <p>Group: {group.name}</p>
          <p>Mentor: {mentor.name}</p>
          <p>Viewer: {viewer.name}</p>
        </div>
      );
      })};
    </div>
  );
};

export default Schedule;
