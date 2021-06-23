const marks = [1, 2, 3.3]

export function getAverage(marks: number[]): number {
    //TODO : calculate the downwar rounded average of the marks array
    const average = (marks: number[]) => marks.reduce((prev: number, curr: number) => prev + curr) / marks.length;
    const result = Math.floor(average(marks))
    return result;
}

getAverage(marks)