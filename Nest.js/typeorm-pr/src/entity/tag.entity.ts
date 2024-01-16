import { Column, Entity, ManyToMany, PrimaryGeneratedColumn } from 'typeorm';
import { PostModel } from './post.entity';
import { UserModel } from './user.entity';

@Entity()
export class TagModel {
  @PrimaryGeneratedColumn()
  id: number;

  @ManyToMany(() => PostModel, (post) => post.tags)
  posts: PostModel[];

  @Column()
  name: string;
}
