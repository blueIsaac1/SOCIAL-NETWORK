export const Fecther = async (configfetch) => {
    const r = await fetch(configfetch.url, {
        method: configfetch.method,
        headers: {
            'Content-Type': 'application/json',
            'Authorization': localStorage.getItem('__token'),
        },
        body: configfetch.data ? JSON.stringify(configfetch.data):null
    })
    const response = await r.json();

    if (r.status == 200){
        console.log('200 zz')
        return response
    } else {
        console.log('fail: ' + response)
    }
        

}