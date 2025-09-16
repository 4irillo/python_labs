export class Tuple {
    constructor(fio, group, gpa)
    {
        //exception
        if (typeof fio !== "string" || typeof group !== "string" || typeof gpa !== "number") throw new TypeError("Failed to construct tuple. Wrong data");
        //code

        //fio
        this.fio = new Set(fio.split(' '));
        this.fio.delete(' ');
        this.fio = new Array(this.fio);
        var secondName = this.fio.values[0];
        var firstName = this.fio.values[1];
        var thirdName = this.fio.values[2];
        var a = secondName + " " + firstName + ". " + thirdName + ".";
        this.fio = a;
        //group
        this.group = group;
        while (group.includes(" "))
        {
            group.delete(" ");
        }
        //gpa
        this.gpa = parseFloat(gpa.toLocaleString(undefined, { minimumFractionDigits: 2 }));
    }

}