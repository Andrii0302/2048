fetch('http://127.0.0.1:5500/',{
    method: 'POST',
    headers: {
        'Content-Type' : 'application/json'
    },
    body: JSON.stringify({
        key: 'up'
    })
}).then(res => {
    if (res.ok) {
        console.log('ok')
    } else{
        console.log('nope')
    }
})
.then(data => console.log(data))
.catch(error => console.log('error'))