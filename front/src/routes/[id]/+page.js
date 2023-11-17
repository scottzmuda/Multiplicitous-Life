export const load = async ({ fetch, params }) => {
    const fetchObservation = async () => {
        const observationRes = await fetch(`http://127.0.0.1:5001/api/o/${params.id}`)
        const observationData = await observationRes.json()
        return observationData
    }
    return {
        item: fetchObservation()
    }
}