export function comp(a1: number[] | null, a2: number[] | null): boolean {
    // null handler
    if (a1) {
        // initialize squared result array
        let c: number[] = []

        // square each element of a1 and push result to c
        a1.forEach((x: number, i: number) => {
            let squared = x ** 2
            c.push(squared)
        })
        // true only if every element is a subset, false otherwise
        if (a2) {
            let result = c.every(v => a2.includes(v))
            if (result === false) {
                return false
            }
        }

        return true
    }
    else {
        return false
    }

}