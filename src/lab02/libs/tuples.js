export class Tuple {
    constructor(fio, group, gpa)
    {
        //exception
        if (typeof fio !== "string" || typeof group !== "string" || typeof gpa !== "number" || gpa < 0 || gpa > 5 || fio.length === 0 || group.length === 0) throw new TypeError("Failed to construct tuple. Wrong data");
        //code

        //fio
        this.fio = Array.from(new Set(fio.split(' ')));
        if (this.fio.indexOf('') !== -1)
            this.fio.splice(this.fio.indexOf(''), 1);
        for (var i = 0; i < this.fio.length; i++){
            var ch = this.fio[i][0].toUpperCase();
            this.fio[i] = ch + this.fio[i].slice(1, this.fio[i].length);
        }
        //group
        this.group = group;
        while (group.includes(" "))
        {
            group.delete(" ");
        }
        //gpa
        this.gpa = gpa.toPrecision(3);
        Object.freeze(this);
    }
    /**
     * 
     */
    format_record() {
        var secondName = this.fio[0];
        var firstNameShort = this.fio[1][0];
        if (this.fio.length === 3){
            var thirdNameShort = this.fio[2][0];
            var a = secondName + " " + firstNameShort + ". " + thirdNameShort + ".";
        }
        else
            var a = secondName + " " + firstNameShort + ".";
        return `${a}, гр. ${this.group}, GPA ${this.gpa}`;
    }


}

export function format_record(array)
{
    if (!Array.isArray(array) || !array.length === 3) throw new TypeError("Wrong data!");
    return  new Tuple(array[0], array[1], array[2]).format_record()

}
