export function comp(a1: number[] | null, a2: number[] | null): boolean {
    // null handler
    
    if (a1.length === 0 || a2.length === 0) {
        return false
    }

    // initialize squared result array
    let c: number[] = []

    // square each element of a1 and push result to c
    a1.forEach((x: number, i: number) => {
        let squared = x ** 2
        c.push(squared)
    })
    // true only if every element is a subset, false otherwise
    let result = c.every(v => a2.includes(v))

    if (result === false) {
        return false
    }

    return true
}

// const a1 = [121, 144, 19, 161, 19, 144, 19, 11]
// const a2 = [132, 14641, 20736, 361, 25921, 361, 20736, 361]

const a1 = [121, 144, 19, 161, 19, 144, 19, 11];
const a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19];

const driver = comp(a1, a2)

console.log(driver)