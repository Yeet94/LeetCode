# Last updated: 6/19/2026, 3:16:04 PM
/**
 * @param {number[][]} grid
 */
function print(grid) {
    console.log("=========")
    for (let i = 0; i < grid.length; i++) {
        let line = ""
        for (let j = 0; j < grid[i].length; j++) {
            let icon;

            switch (grid[i][j]) {
                case 0: icon = "⬛"; break;
                case 1: icon = "🍊"; break;
                case 2: icon = "🪰"; break;
            }

            line += icon + " "
        }
        console.log(line)
    }
    console.log("=========")

}