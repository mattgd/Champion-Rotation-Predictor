export type Champion = {
    id: number,
    name: string,
    key: string,
    subclass: string,
    blueEssence: number,
    riotPoints: number,
    dateReleased: string,
    image: string,
}

export type Rotation = {
    weekNumber: number,
    startDate: string,
    endDate: string,
}
