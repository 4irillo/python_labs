import * as arrays from "./arrays.js"

export function transpose(a){
    //exceptions
    if (!(a instanceof Array)) throw new TypeError("TypeError");
    if (a.length === 0) return [];
    if (a.length !== 0) var l = a[0].length
    for (var i of a) if (i.length != l) throw new TypeError("ValueError");

    //actual code
    var ans = [];
    var m = a.length;
    var n = a[0].length;
    for (var i = 0; i < n; i++)
    {
        let temp = []
        for (var j = 0; j < m; j++)
            temp.push(a[j][i]);
        ans.push(temp);
        temp = [];
    }
    return ans;
}


export function row_sums(a){
    //exceptions
    if (!(a instanceof Array)) throw new TypeError("TypeError");
    if (a.length === 0) return [];
    if (a.length !== 0) var l = a[0].length
    for (var i of a) if (i.length != l) throw new TypeError("ValueError");

    //actual code
    var ans = []
    for (var i of a) {
        var sum = 0;
        for (var j of i)
            sum+=j;
        ans.push(sum)
    }
    return ans

}

export function col_sums(a){
    //exceptions
    if (!(a instanceof Array)) throw new TypeError("TypeError");
    if (a.length === 0) return [];
    if (a.length !== 0) var l = a[0].length
    for (var i of a) if (i.length != l) throw new TypeError("ValueError");

    //actual code
    var ans = []
    for (var m = 0; m < a[0].length; m++)
    {
        var temp = 0;
        for (var n = 0; n < a.length; n++)
            temp += a[n][m];
        ans.push(temp);
    }
    return ans

}