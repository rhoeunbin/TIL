import {
  Column,
  Entity,
  JoinTable,
  ManyToMany,
  ManyToOne,
  PrimaryGeneratedColumn,
} from 'typeorm';
import { UserModel } from './user.entity';
import { TagModel } from './tag.entity';

@Entity()
export class PostModel {
  @PrimaryGeneratedColumn()
  id: number;

  @ManyToOne(() => UserModel, (user) => user.posts)
  // manytoone인 경우는 복수 사용 가능!
  author: UserModel;

  @ManyToMany(() => TagModel, (tag) => tag.posts)
  @JoinTable()
  tags: TagModel[];

  @Column()
  title: string;
}
