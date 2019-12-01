export interface IPart {
  name: string;
  type: IType;
  optional?: boolean;
}

export enum IType {
  BATTERY,
  SCREEN,
  CPU,
  MEMORY,
  HARD_DRIVE
}
