#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

function groupById (todos) {
  const groups = todos.reduce((group, todo) => {
    const { userId } = todo;
    group[userId] = group[userId] || [];
    group[userId].push(todo);
    return group;
  }, {});
  return groups;
}

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    const todos = JSON.parse(body);
    const completed = todos.filter(todo => todo.completed === true);
    const taskSummary = {};
    const groupedTasks = groupById(completed);
    for (const task in groupedTasks) {
      taskSummary[task] = groupedTasks[task].length;
    }
    console.log(taskSummary);
  } else {
    console.log(`code: ${res.statusCode}`);
  }
});
