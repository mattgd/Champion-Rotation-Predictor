export type Champion = {
    id: number,
    name: string,
    key: string,
    title: string,
    tags: string,
    dateReleased: string,
    image: string,
}

export type Rotation = {
    weekNumber: number,
    startDate: string,
    endDate: string,
}
