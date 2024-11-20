const BASE_API = "http://localhost:8000"

export const Fecther = async (configFetch) => {
    const r = await fetch(BASE_API + configFetch.url, {
        method: configFetch.method,
        headers: {
            'Content-Type': 'application/json',
            'Authorization': localStorage.getItem('__token'),
        },
        body: configFetch.data ? JSON.stringify(configFetch.data):null
    })
    const response = await r.json();

    if (r.status == 200){
        console.log('200 zz')
        return response
    } else {
        console.log('fail: ' + response)
    }
        

}