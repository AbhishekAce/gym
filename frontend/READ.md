# Frontend Integration

You can use any frontend framework (e.g., React, Vue) and connect to the FastAPI server at `/` or `/step`.

Example React fetch:
```js
fetch("http://localhost:8000/step", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ action: "move" }),
})
  .then(res => res.json())
  .then(data => console.log(data));
```
