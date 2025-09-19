function min(a, b) {
    //exceptions
    if (typeof(a) !== "number" || typeof(b) !== "number") throw new TypeError("ParamError");
    //code
    if (a < b) return a;
    else return b;
}


function max(a, b) {
    //exceptions
    if (typeof(a) !== "number" || typeof(b) !== "number") throw new TypeError("ParamError");
    //code
    if (a > b) return a;
    else return b;
}

function comp(a, b){return (a - b)}



export function min_max(a) {
    //exceptions
    if (!(a instanceof Array)) throw new TypeError("TypeError");
    if (a.length === 0) throw new Error("ValueError");
    //code
    var mn = 1e7, mx = -1e7;
    for (var i of a) {
        mn = min(i, mn);
        mx = max(i, mx);
    }
    return [mn, mx];
}



export function unique_sorted(a) {
    //exceptions
    if (!(a instanceof Array)) throw new TypeError("TypeError");
    //code    
    a.sort(comp);
    return Array.from(new Set(a));
}

export function flatten(a)
{
    //exceptions
    if (!(a instanceof Array)) throw new TypeError("TypeError");
    //code
    let b = [];
    for (var i of a)
    {
        if (!(i instanceof Array) && !(i instanceof Set)) throw new TypeError("TypeError");
        for (var j of i) b.push(j);
    }
    return b;
}
