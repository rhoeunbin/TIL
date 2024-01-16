import { Controller, Delete, Get, Param, Patch, Post } from '@nestjs/common';
import { AppService } from './app.service';
import { InjectRepository } from '@nestjs/typeorm';
import { Role, UserModel } from './entity/user.entity';
import {
  Between,
  ILike,
  In,
  LessThan,
  LessThanOrEqual,
  Like,
  MoreThan,
  MoreThanOrEqual,
  Not,
  Repository,
} from 'typeorm';
import { ProfileModel } from './entity/profile.entity';
import { PostModel } from './entity/post.entity';
import { TagModel } from './entity/tag.entity';

@Controller()
export class AppController {
  constructor(
    @InjectRepository(UserModel)
    private readonly userRepository: Repository<UserModel>,
    @InjectRepository(ProfileModel)
    private readonly profileRepository: Repository<ProfileModel>,
    @InjectRepository(PostModel)
    private readonly postRepository: Repository<PostModel>,
    @InjectRepository(TagModel)
    private readonly tagRepository: Repository<TagModel>,
  ) {}

  @Post('sample')
  async sample() {
    // create -> 모델에 해당되는 객체 생성 - 저장은 안함
    // const user1 = await this.userRepository.create({
    //   email: 'test@code.ai',
    // });

    // save -> 저장
    // const user2 = await this.userRepository.save({
    //   email: 'test@code.ai',
    // });

    // preload
    // 입력된 값을 기반으로 데이터베이스에 있는 데이터를 불러오고 추가 입력된 값으로 데이터베이스에서 가져온 값을들 대체함, 저장하지는 않음
    // const user3 = await this.userRepository.preload({
    //   id: 201,
    //   email: 'test@code.aaaaaaa',
    // });

    // delete -> 삭제
    // await this.userRepository.delete(201);

    // await this.userRepository.increment(
    //   {
    //     id: 1,
    //   },
    //   'count',
    //   2,
    // );

    // await this.userRepository.decrement(
    //   {
    //     id: 1,
    //   },
    //   'count',
    //   1,
    // );

    // count -> 개수 카운팅 하기
    // const count = await this.userRepository.count({
    //   where: {
    //     email: ILike('%0%'),
    //   },
    // });

    // sum -> 더함
    // const sum = await this.userRepository.sum('count', {
    //   email: ILike('%0%'),
    // });

    // average -> 평균
    // const average = await this.userRepository.average('count', {
    //   id: LessThan(4),
    // });

    // min -> 최소
    const min = await this.userRepository.minimum('count', {
      id: LessThan(4),
    });

    // max -> 최대
    const max = await this.userRepository.maximum('count', {
      id: LessThan(4),
    });

    // // find -> 전체조회
    // const users = await this.userRepository.find({});

    // // findOne -> 하나의 값 조회 => 여러개면 가장 첫번째값 조회
    // const userOne = await this.userRepository.findOne({
    //   where: {
    //     id: 3,
    //   },
    // });

    // 값들을 찾고 몇개의 전체값이 있는지 필터하는 방법
    const usersAndCount = await this.userRepository.findAndCount({
      take: 3,
    });

    return usersAndCount;
  }

  @Post('users')
  async postUser() {
    for (let i = 0; i < 100; i++) {
      await this.userRepository.save({
        // role: Role.ADMIN,
        email: `user-${i}@gmail.com`,
      });
    }
  }

  @Get('users')
  getUsers() {
    return this.userRepository.find({
      // 어떤 프로퍼티를 선택할지
      // select를 정의하지 않으면 모든 프로퍼티를 가져옴(기본)
      // select를 정의하면 정의된 프로퍼티들만 가져옴
      // select: {
      //   id: true,
      //   createdAt: true,
      //   version: true,
      //   profile: {
      //     id: true,
      //   },
      // },

      // 필터링할 조건 가져옴
      where: {
        // 아닌 경우 가져오기
        // id: Not(1),
        // 적은 경우
        // id: LessThan(30),
        // 적거나 같은 경우
        // id: LessThanOrEqual(30),
        // 많은 경우
        // id: MoreThan(30),
        // // 많거나 같은 경우
        // id: MoreThanOrEqual(30),
        // // 같은 경우
        // id: Equal(30),
        // 사이값
        // id: Between(10, 15),
        // 해당되는 여러개의 값
        // id: In([1, 3, 4]),
        // 유사값
        //email: Like('%0%'),
        // 대소문자 구별 없는 유사값
        // email: iLike('%GMAIL%'),
        //   profile: {
        //     id: 5,
        //   },
      },

      // // 관계 가져오기
      // relations: {
      //   profile: true,
      // },

      // // 오름차 ASC / 내림차 DESC
      // order: {
      //   id: 'DESC',
      // },

      // // 처음 몇개를 제외할지
      // // 기본값 : 0
      // skip: 0,

      // // 몇 개를 가져올지
      // // 기본값 : 0 => table 전체
      // take: 1,
    });
  }

  @Patch('users/:id')
  async patchUser(@Param('id') id: string) {
    const user = await this.userRepository.findOne({
      where: {
        id: parseInt(id),
      },
    });
    return this.userRepository.save({
      ...user,
    });
  }

  @Post('user/profile')
  async createUserAndProfile() {
    const user = await this.userRepository.save({
      // email: 'dmsqls@never.co',
      // profile: { profileImg: 'smil.png' },
    });
    // const profile = await this.profileRepository.save({
    //   profileImg: 'smile.png',
    //   user,
    // });
    return user;
  }

  @Delete('user/profile/:id')
  async deleteProfile(@Param('id') id: string) {
    await this.profileRepository.delete(+id);
  }

  @Post('user/post')
  async createUserAndPosts() {
    const user = await this.userRepository.save({
      email: 'eunbin',
    });
    await this.postRepository.save({
      author: user,
      title: 'post1',
    });
    await this.postRepository.save({
      author: user,
      title: 'post2',
    });
    return user;
  }

  @Post('posts/tags')
  async createPostsTags() {
    const post1 = await this.postRepository.save({
      title: 'tag test 1',
    });
    const post2 = await this.postRepository.save({
      title: 'tag test 2',
    });
    const tag1 = await this.tagRepository.save({
      name: 'javascript',
      posts: [post1, post2],
    });
    const tag2 = await this.tagRepository.save({
      name: 'typescript',
      posts: [post1],
    });
    const post3 = await this.postRepository.save({
      title: 'nextjs lecture',
      tags: [tag1, tag2],
    });
    return true;
  }

  @Get('posts')
  getPosts() {
    return this.postRepository.find({
      relations: {
        tags: true,
      },
    });
  }

  @Get('tags')
  getTags() {
    return this.tagRepository.find({
      relations: {
        posts: true,
      },
    });
  }
}
function IN(arg0: number[]): number | import('typeorm').FindOperator<number> {
  throw new Error('Function not implemented.');
}
