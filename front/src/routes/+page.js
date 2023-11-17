export const load = async ({ fetch }) => {
    const fetchObservation = async () => {
        const observationRes = await fetch(`http://127.0.0.1:5001/api/o`)
        const observationData = await observationRes.json()
        return observationData
    }
    return {
        items: fetchObservation()
    }
}