import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'tempConv'
})
export class TempConvPipe implements PipeTransform {

  transform(value: any, args?: any): any {
    if (args[0] == 'C')
        return (value - 273.15).toFixed(1) + "°C";
    if (args[0] == 'F'){
        let temp = (value - 273.15) * (9 / 5) + 32;
        return temp.toFixed(1) + "°F";
    }


  }

}
