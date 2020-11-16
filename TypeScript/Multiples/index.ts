// Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
// Note: If the number is a multiple of both 3 and 5, only count it once. Also, if a number is negative, return 0(for languages that do have them)


export class Challenge {
    static solution(number: number) {
        // if number is negative return 0
        if (number < 0) {
            return 0
        }

        let x = 3
        let y = 5

        // multiples arrays
        let threeSumArray: number[] = []
        let fiveSumArray: number[] = []

        // calculate and push all multiples while it is less than number for both
        while (x < number) {
            x = x + 3
            threeSumArray.push(x)
        }
        while (y < number) {
            y = y + 5
            fiveSumArray.push(y)
        }

        // deduplicate array
        var threeFive = threeSumArray.concat(fiveSumArray.filter((item) => threeSumArray.indexOf(item) < 0))

        // sum using reducer
        const reducer = (accumulator: number, currentValue: number) => accumulator + currentValue;
        let sum = threeFive.reduce(reducer)

        console.log(sum)
        return sum
    }
}

console.log(Challenge.solution(5))