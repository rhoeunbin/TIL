import {
  Column,
  CreateDateColumn,
  Entity,
  Generated,
  JoinColumn,
  OneToMany,
  OneToOne,
  PrimaryColumn,
  PrimaryGeneratedColumn,
  UpdateDateColumn,
  VersionColumn,
} from 'typeorm';
import { ProfileModel } from './profile.entity';
import { profile } from 'console';
import { PostModel } from './post.entity';

export enum Role {
  USER = 'user',
  ADMIN = 'admin',
}

@Entity()
export class UserModel {
  // @PrimaryGeneratedColumn()
  // 자동으로 id를 생성하는 역할
  // 순서대로 위로 올라감 1, 2, 3,4 -> 9999

  // PrimaryColumn은 모든 테이블에서 기본적으로 존재해야함
  // 테이블 안에서 각각의 Row를 구분할 수 있는 컬럼

  // @PrimaryColumn()
  // 주가 되는 컬럼
  // 사용자가 직접 넣어야함

  // @PrimaryGeneratedColumn('uuid')
  // UUID -> asdfa1231412-1241234asfksda-1412szsadf

  // id
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  email: string;

  // @Column({
  //   type: 'varchar',
  //   // db에서 인지하는 칼럼 타입
  //   // 자동으로 유추됨

  //   name: 'title',
  //   // 데이터베이스 칼럼 이름
  //   // 프로퍼티 이름으로 자동 유추됨

  //   length: 300,
  //   // 값의 길이
  //   // 입력할 수 있는 글자의 길이가 300

  //   nullable: true,
  //   // null이 가능한지

  //   update: true,
  //   // true면 처음 저장할 때만 값 지정 가능
  //   // 이후에는 값 변경 불가능

  //   select: false,
  //   // 기본값이 true
  //   // find()를 실행할 때 기본으로 값을 불러올지

  //   default: 'default value',
  //   // 기본 값이 되는 것
  //   // 아무것도 입력하지 않았을 때 저장되는 값

  //   unique: false,
  //   // 기본값이 false
  //   // 칼럼 중에서 유일무이한 값이 돼야하는지
  // })
  // title: string;

  @Column({
    type: 'enum',
    enum: Role,
    default: Role.USER,
  })
  role: Role;

  // 데이터 생성 일자
  // 데이터가 생성되는 날짜와 시간이 자동으로 찍힘
  @CreateDateColumn()
  createdAt: Date;

  // 데이터 업데이트
  // 데이터가 업데이트 되는 날짜와 시간이 자동으로 찍힘
  @UpdateDateColumn()
  updatedAt: Date;

  // 데이터가 업데이트 될때마다 1씩 올라간다
  // 처음 생성되면 값은 1
  // save() 함수가 몇 번 불렸는지 기억
  @VersionColumn()
  version: number;

  @Column()
  @Generated('increment') // primary는 아니지만 데이터가 생성될 때마다 자동으로 1씩 넣어줌
  additionId: number;

  @Column()
  @Generated('uuid') // primary는 아니지만 데이터가 생성될 때마다 자동으로 uuid 넣어줌
  additionUuid: string;

  @OneToOne(() => ProfileModel, (profile) => profile.user, {
    eager: false,
    // find() 실행할때마다 항상 같이 가져올 relation

    cascade: true,
    // 저장할 때 relation을 한번에 같이 저장 가능

    nullable: true,
    // null이 가능한지

    onDelete: 'CASCADE',
    // 관계가 삭제됐을 때
    // no action -> 아무것도 안 함
    // cascade -> 참조하는 row도 같이 삭제
    // set null -> 참조하는 row에서 참조 id를 null로 변경
    // set default -> 기본 세팅으로 설정 (테이블의 기본 세팅)
    // restrict -> 참조하고 있는 row가 있는경우 참조 당하는 row 삭제 불가
  })
  @JoinColumn()
  profile: ProfileModel;

  @OneToMany(() => PostModel, (post) => post.author)
  posts: PostModel[];

  @Column({
    default: 0,
  })
  count: number;
}
